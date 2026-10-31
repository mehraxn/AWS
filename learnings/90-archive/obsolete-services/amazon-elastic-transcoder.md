# Archived note

> **Archive notice (checked 2026-07-21):** Amazon Elastic Transcoder support ended on November 13, 2025. AWS Elemental MediaConvert is the verified migration destination.

# Amazon Elastic Transcoder

## Simple definition

Amazon Elastic Transcoder was an AWS service that converted video and audio files from one format into another.

It helped businesses prepare media files so they could play on different devices like phones, tablets, browsers, and TVs.

## Core idea in plain English

Think of Amazon Elastic Transcoder like a video format converter in the cloud.

You upload a media file, tell AWS what output format you want, and AWS creates a new version that works for the device or app you need.

## Main use cases

 Convert uploaded videos into web and mobile-friendly formats
 Create multiple versions of the same video for different screen sizes
 Generate thumbnails from videos
 Prepare video-on-demand content for apps and websites
 Automate media processing instead of doing it manually on your own servers

## Key features

 Fully managed transcoding service
 Works with media files stored in Amazon S3
 Uses pipelines to manage transcoding workflows
 Uses presets to define output settings
 Can create multiple output files from one input file
 Can generate thumbnails
 Supports encryption and integration with AWS KMS
 Can be monitored with Amazon CloudWatch

## How it works

Here is the simple flow

1. You upload an input video file to Amazon S3.
2. You create a pipeline that tells Elastic Transcoder where to get the input and where to place the output.
3. You choose a preset, which defines the output format, resolution, codec, and other settings.
4. You submit a job.
5. Elastic Transcoder processes the file and stores the converted output back in Amazon S3.
6. Your app or website can then deliver the output video to users.

## Why it is important for the exam

For the exam, the main idea is to recognize that Elastic Transcoder is a media transcoding service.

It was designed for file-based video and audio conversion, not for live streaming, not for storage, and not for content delivery.

Also, this is a very important modern exam note

Amazon Elastic Transcoder was discontinued on November 13, 2025.

That means if an exam question asks for the current AWS service for modern file-based video transcoding, the better answer is usually AWS Elemental MediaConvert.

So you should know Elastic Transcoder mainly as

 a legacy AWS media conversion service
 a service that used pipelines, presets, and jobs
 something often compared with MediaConvert

## Related AWS services and differences

### AWS Elemental MediaConvert

This is the most important related service.

 Elastic Transcoder older, simpler file-based transcoding service
 MediaConvert newer, more advanced file-based video transcoding service

For modern AWS architecture questions, MediaConvert is usually the better answer.

### Amazon S3

 S3 stores the input and output files
 Elastic Transcoder does the conversion work

S3 is storage. Elastic Transcoder is processing.

### Amazon CloudFront

 CloudFront delivers videos to users globally
 Elastic Transcoder prepares the video files before delivery

CloudFront is delivery. Elastic Transcoder is conversion.

### Amazon CloudWatch

 CloudWatch monitors jobs and service metrics
 Elastic Transcoder performs the media conversion

### Amazon SNS

 SNS can be used to send notifications when jobs complete or fail
 Elastic Transcoder does not replace SNS

## Common exam traps

### Trap 1 Confusing it with MediaConvert

This is the biggest trap.

If the question is about a modern AWS solution for file-based media transcoding, choose AWS Elemental MediaConvert, not Elastic Transcoder.

### Trap 2 Thinking it is for live streaming

Elastic Transcoder is mainly for file-based transcoding.

It is not the main answer for live video streaming workflows.

### Trap 3 Thinking S3 does the transcoding

S3 stores files. It does not convert video formats.

### Trap 4 Thinking CloudFront converts the video

CloudFront distributes content. It does not transcode media files.

### Trap 5 Thinking it runs on your own servers

Elastic Transcoder was a managed AWS service, so AWS handled the infrastructure.

## Easy real-world example

A training company uploads one master video file to Amazon S3.

The company wants

 one version for mobile phones
 one version for tablets
 one version for desktop users
 thumbnail images for the course catalog

Elastic Transcoder takes the original file, converts it into the needed versions, saves the outputs in S3, and the company then delivers them to learners through its website.

## Final summary

Amazon Elastic Transcoder was an AWS managed service for converting media files into different formats.

Its main purpose was to help businesses prepare video and audio files for different devices and playback needs.

For exam study, remember the core workflow
S3 input - pipeline - preset - job - S3 output

But also remember the modern exam reality
Elastic Transcoder is a legacy service, and AWS Elemental MediaConvert is the newer service you should usually choose today.

## Short exam answer

Amazon Elastic Transcoder was a managed AWS service for file-based media transcoding. It converted video and audio files into formats suitable for different devices and stored input and output files in Amazon S3. For modern AWS solutions, AWS Elemental MediaConvert is usually the preferred service.

## Memory trick

Elastic Transcoder = “Translate my video into other formats.”

And remember
Old converter = Elastic Transcoder
Modern converter = MediaConvert
