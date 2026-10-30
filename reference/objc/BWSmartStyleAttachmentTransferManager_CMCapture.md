# `BWSmartStyleAttachmentTransferManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _inferences;
@"NSMutableDictionary" _attachedMedia;
@"NSMutableDictionary" _attachments;
B _hasNecessaryAttachments;
^{opaqueCMSampleBuffer=} _styledBuffer;
```

## Properties

```
@property (TB,N,V_hasNecessaryAttachments) hasNecessaryAttachments;
@property (TB,R,N) isEmpty;
@property (TB,R,N) readyToTransfer;
@property (T^{opaqueCMSampleBuffer=},R,N) styledSbufWithAttachmentsTransferred;
```

## Class methods

```
+[BWSmartStyleAttachmentTransferManager initialize];
```

## Instance methods

```
-[BWSmartStyleAttachmentTransferManager init];
-[BWSmartStyleAttachmentTransferManager dealloc];
-[BWSmartStyleAttachmentTransferManager reset];
-[BWSmartStyleAttachmentTransferManager isEmpty];
-[BWSmartStyleAttachmentTransferManager readyToTransfer];
-[BWSmartStyleAttachmentTransferManager enqueueStyledSampleBuffer:];
-[BWSmartStyleAttachmentTransferManager enqueueUnstyledSampleBuffer:];
-[BWSmartStyleAttachmentTransferManager hasNecessaryAttachments];
-[BWSmartStyleAttachmentTransferManager setHasNecessaryAttachments:];
-[BWSmartStyleAttachmentTransferManager styledSbufWithAttachmentsTransferred];
```
