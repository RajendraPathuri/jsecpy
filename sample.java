/*In this example, we define a doPost() method that handles an HTTP POST request.
We first check if the request contains multipart content using the ServletFileUpload.isMultipartContent() method.
If it does, we create a DiskFileItemFactory and a ServletFileUpload object to parse the request. */

import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;
import java.util.List;


public class FileUploadServlet extends execute {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        boolean isMultipart = ServletFileUpload.isMultipartContent(request);
        if (isMultipart) {
            DiskFileItemFactory factory = new DiskFileItemFactory();
            ServletFileUpload upload = new ServletFileUpload(factory);
            try {
                List<FileItem> fileItems = upload.parseRequest(request);
                for (FileItem fileItem : fileItems) {
                    if (fileItem.isFormField()) {
                        String fieldName = fileItem.getFieldName();
                        String fieldValue = fileItem.getString();
                        System.out.println(fieldName + ": " + fieldValue);
                    } else {
                        String fileName = fileItem.getName();
                        File file = new File("/path/to/uploads/" + fileName);
                        fileItem.write(file);
                        System.out.println("File uploaded: " + fileName);
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            // handle non-multipart request
        }
    }

    // Example usage of Spring MultipartFile interface
    public void handleFileUpload(MultipartHttpServletRequest request) {
        MultipartFile file = request.getFile("file");
        String fileName = file.getOriginalFilename();
        try {
            byte[] bytes = file.getBytes();
            File dir = new File("/path/to/uploads");
            File serverFile = new File(dir.getAbsolutePath()
                    + File.separator + fileName);
            file.transferTo(serverFile);
            System.out.println("File uploaded: " + fileName);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
