import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_path, output_folder, zoom_x=2, zoom_y=2):
    """
    将 PDF 文件转换为图片
    :param pdf_path: PDF 文件路径
    :param output_folder: 输出图片的文件夹
    :param zoom_x: 水平缩放比例（提高分辨率）
    :param zoom_y: 垂直缩放比例（提高分辨率）
    """
    # 打开 PDF 文件
    pdf_document = fitz.open(pdf_path)

    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历每一页
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # 加载页面
        mat = fitz.Matrix(zoom_x, zoom_y)  # 设置缩放比例
        pix = page.get_pixmap(matrix=mat)  # 渲染为图像

        # 保存图像
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        pix.save(image_path)
        print(f"已保存: {image_path}")

    print("转换完成！")

# 示例调用
pdf_path = "2.0response.pdf"  # 替换为你的 PDF 文件路径
output_folder = "output_images"  # 输出图片的文件夹
pdf_to_images(pdf_path, output_folder)