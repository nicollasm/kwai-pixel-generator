# This function generates the pixel script for the Tiktok Ads platform.
def generate_pixel_script(pixel_id, event):
    return f"<script>\n    ttq.track('{event}');\n</script>"
