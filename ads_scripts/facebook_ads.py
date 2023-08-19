# This function generates the pixel script for the Facebook Ads platform.
def generate_pixel_script(pixel_id, event):
    return f"<script>\n    fbq('track', '{event}');\n</script>"
