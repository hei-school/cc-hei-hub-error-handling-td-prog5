package com.fileUpload.demo.service;

import com.fileUpload.demo.entity.Attachment;
import com.fileUpload.demo.repository.AttachmentRepository;
import com.fileUpload.demo.service.errorHandler.Handler;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;

@Service
public class AttachmentServiceImpl implements AttachmentService{
    private AttachmentRepository attachmentRepository;
    private Handler handler;
    public AttachmentServiceImpl(AttachmentRepository attachmentRepository) {
        this.attachmentRepository = attachmentRepository;
    }
    @Override
    public Attachment saveAttachment(MultipartFile file) throws Exception {
        String fileName = StringUtils.cleanPath(file.getOriginalFilename());
        try {
            if (fileName.contains("..")) {
                throw new Exception("filename contains invalid path sequence" + fileName);
            }

            Attachment attachment
                    = new Attachment(fileName,
                    file.getContentType(),
                    file.getBytes());
            return attachmentRepository.save(attachment);
        }catch (Exception e) {
            Handler.handleError(e);

            throw new Exception("Could not save File: " + fileName);
        }
    }

    @Override
    public Attachment getAttachment(String fileID) throws Exception {
        return attachmentRepository
                .findById(fileID)
                .orElseThrow(() -> new Exception("File not found with Id: " + fileID));
    }
}
