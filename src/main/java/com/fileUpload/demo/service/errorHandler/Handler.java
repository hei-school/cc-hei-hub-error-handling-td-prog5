package com.fileUpload.demo.service.errorHandler;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.Date;
@Service
public class Handler {
    public static void handleError(Exception e) {
        logErrorToFile(e);
        e.printStackTrace();
    }

    public static void logErrorToFile(Exception e) {
        String fileName = "error_" + e.getClass().getSimpleName() + ".log";

        try (PrintWriter writer = new PrintWriter(new FileWriter(fileName, true))) {
            // Logging the timestamp and code line in the log
            writer.println(new Date() + " - Error: " + e.getMessage());
            writer.println("Code line: " + e.getStackTrace()[0].toString());
            writer.println("-----------");

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

}
