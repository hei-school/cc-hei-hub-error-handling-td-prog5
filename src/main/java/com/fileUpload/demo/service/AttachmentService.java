package com.fileUpload.demo.service;

import com.fileUpload.demo.entity.Attachment;
import org.springframework.web.multipart.MultipartFile;

public interface AttachmentService {
    Attachment saveAttachment(MultipartFile file) throws Exception;

    Attachment getAttachment(String fileID) throws Exception;
}
