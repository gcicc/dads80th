"""Resize all images in images/ to web-friendly resolution (max 1200px wide).

Reads from images/, writes resized versions back in-place.
Originals are preserved in dads80th-pics/ (already exists as the source archive).

Usage: python scripts/resize_images.py [--max-width 1200] [--quality 82] [--dry-run]
"""

import argparse
import os
from pathlib import Path

from PIL import Image

IMAGES_DIR = Path(__file__).resolve().parent.parent / "images"
SUPPORTED = {".jpg", ".jpeg", ".png"}


def resize_image(path: Path, max_width: int, quality: int, dry_run: bool) -> dict:
    """Resize a single image. Returns stats dict."""
    original_size = path.stat().st_size

    try:
        with Image.open(path) as img:
            orig_w, orig_h = img.size

            if orig_w <= max_width:
                return {"path": path, "skipped": True, "reason": f"already {orig_w}px wide"}

            ratio = max_width / orig_w
            new_h = int(orig_h * ratio)

            if dry_run:
                return {
                    "path": path,
                    "skipped": False,
                    "dry_run": True,
                    "orig_size": original_size,
                    "orig_dims": (orig_w, orig_h),
                    "new_dims": (max_width, new_h),
                }

            resized = img.resize((max_width, new_h), Image.LANCZOS)

            # Preserve EXIF orientation if present
            exif = img.info.get("exif")

            save_kwargs = {"quality": quality, "optimize": True}
            if exif:
                save_kwargs["exif"] = exif

            if path.suffix.lower() == ".png":
                resized.save(path, "PNG", optimize=True)
            else:
                resized.save(path, "JPEG", **save_kwargs)

            new_size = path.stat().st_size
            return {
                "path": path,
                "skipped": False,
                "orig_size": original_size,
                "new_size": new_size,
                "orig_dims": (orig_w, orig_h),
                "new_dims": (max_width, new_h),
                "saved": original_size - new_size,
            }
    except Exception as e:
        return {"path": path, "skipped": True, "reason": f"error: {e}"}


def main():
    parser = argparse.ArgumentParser(description="Resize images for web")
    parser.add_argument("--max-width", type=int, default=1200)
    parser.add_argument("--quality", type=int, default=82)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    images = sorted(
        p
        for p in IMAGES_DIR.rglob("*")
        if p.is_file() and p.suffix.lower() in SUPPORTED
    )

    print(f"Found {len(images)} images in {IMAGES_DIR}")
    print(f"Max width: {args.max_width}px, JPEG quality: {args.quality}")
    if args.dry_run:
        print("DRY RUN — no files will be modified\n")
    print()

    total_saved = 0
    resized_count = 0
    skipped_count = 0

    for img_path in images:
        result = resize_image(img_path, args.max_width, args.quality, args.dry_run)
        rel = img_path.relative_to(IMAGES_DIR)

        if result.get("skipped"):
            skipped_count += 1
            print(f"  SKIP  {rel} ({result.get('reason', '')})")
        elif result.get("dry_run"):
            resized_count += 1
            orig_kb = result["orig_size"] / 1024
            print(
                f"  WOULD {rel}: {result['orig_dims'][0]}x{result['orig_dims'][1]} -> "
                f"{result['new_dims'][0]}x{result['new_dims'][1]} ({orig_kb:.0f} KB)"
            )
        else:
            resized_count += 1
            saved = result["saved"]
            total_saved += saved
            print(
                f"  DONE  {rel}: {result['orig_dims'][0]}x{result['orig_dims'][1]} -> "
                f"{result['new_dims'][0]}x{result['new_dims'][1]}  "
                f"{result['orig_size']//1024}KB -> {result['new_size']//1024}KB "
                f"(saved {saved//1024}KB)"
            )

    print(f"\nResized: {resized_count}, Skipped: {skipped_count}")
    if not args.dry_run:
        print(f"Total saved: {total_saved / 1048576:.1f} MB")


if __name__ == "__main__":
    main()
