
"""Các hàm tiền xử lý văn bản dùng chung."""

import re
import math


def clean_text(value):
    """Chuẩn hóa văn bản trước khi vector hóa."""

    if value is None or (
        isinstance(value, float) and math.isnan(value)
    ):
        return ""

    text = str(value).lower()

    # Xử lý URL
    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )

    # Xử lý ký tự đặc biệt, giữ từ và dấu nháy
    text = re.sub(
        r"[^\w\s']",
        " ",
        text,
        flags=re.UNICODE
    )

    # Loại bỏ khoảng trắng thừa
    text = re.sub(r"\s+", " ", text).strip()

    return text
