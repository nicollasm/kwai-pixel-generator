# This function generates the pixel script for the Kwai Ads platform.
def generate_pixel_script(pixel_id, event):
    return f"<script>\n    kwaiq.instance('{pixel_id}').track('{event}');\n</script>"
