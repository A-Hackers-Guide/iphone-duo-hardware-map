# `BWDeferredContainer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 18 properties, 25 instance methods, 9 class methods

## Instance variables

```
q _creationTimeNS;
{_opaque_pthread_rwlock_t="__sig"q"__opaque"[192c]} _lock;
@"NSURL" _baseFolderURL;
@"NSString" _applicationID;
@"NSString" _captureRequestIdentifier;
q _manifestVersion;
@"BWStillImageSettings" _stillImageSettings;
@"BWDeferredPipelineParameters" _pipelineParameters;
@"NSMutableArray" _intermediates;
@"NSMutableArray" _photoDescriptors;
@"NSArray" _bufferAttributes;
```

## Properties

```
@property (TI,R,N) processingType;
@property (T@"NSURL",R,N,V_baseFolderURL) baseFolderURL;
@property (T@"NSString",R,N) applicationID;
@property (T@"NSString",R,N,V_captureRequestIdentifier) captureRequestIdentifier;
@property (TQ,R,N) captureRequestIdentifierBytesLow;
@property (TQ,R,N) captureRequestIdentifierBytesHigh;
@property (Tq,R,N,V_manifestVersion) manifestVersion;
@property (T@"NSDictionary",R,N) manifest;
@property (T@"NSArray",R,N,V_photoDescriptors) photoDescriptors;
@property (T@"BWDeferredPipelineParameters",R,N,V_pipelineParameters) pipelineParameters;
@property (T@"BWStillImageSettings",R,N,V_stillImageSettings) stillImageSettings;
@property (T@"BWStillImageCaptureSettings",R,N) captureSettings;
@property (T@"FigCaptureStillImageSettings",R,N) settings;
@property (T@"BWStillImageProcessingSettings",R,N) processingSettings;
@property (T@"NSArray",R,N,V_bufferAttributes) bufferAttributes;
@property (T@"NSArray",R,N) intermediates;
@property (T@"NSArray",R,N) attachedMediaKeys;
@property (T@"NSString",R,N) prettyDescription;
```

## Class methods

```
+[BWDeferredContainer initialize];
+[BWDeferredContainer archiveObject:error:];
+[BWDeferredContainer archiveObjectWithURL:object:error:];
+[BWDeferredContainer buildArchiveClasses:];
+[BWDeferredContainer manifestDictionaryForApplicationIdentifier:captureRequestIdentifier:photoDescriptors:];
+[BWDeferredContainer manifestDictionaryForURL:err:];
+[BWDeferredContainer unarchiveObject:classes:error:];
+[BWDeferredContainer unarchiveObjectWithURL:classes:error:];
+[BWDeferredContainer validateManifestURLSize:];
```

## Instance methods

```
-[BWDeferredContainer applicationID];
-[BWDeferredContainer stillImageSettings];
-[BWDeferredContainer hasTag:];
-[BWDeferredContainer init];
-[BWDeferredContainer settings];
-[BWDeferredContainer prettyDescription];
-[BWDeferredContainer dealloc];
-[BWDeferredContainer captureRequestIdentifier];
-[BWDeferredContainer description];
-[BWDeferredContainer pipelineParameters];
-[BWDeferredContainer manifestVersion];
-[BWDeferredContainer manifest];
-[BWDeferredContainer captureSettings];
-[BWDeferredContainer initWithApplicationID:resolvedSettings:unresolvedSettings:processingSettings:pipelineParameters:intermediates:photoDescriptors:];
-[BWDeferredContainer attachedMediaKeys];
-[BWDeferredContainer baseFolderURL];
-[BWDeferredContainer bufferAttributes];
-[BWDeferredContainer captureRequestIdentifierBytesHigh];
-[BWDeferredContainer captureRequestIdentifierBytesLow];
-[BWDeferredContainer initWithApplicationID:captureRequestIdentifier:baseFolderURL:queuePriority:err:];
-[BWDeferredContainer intermediates];
-[BWDeferredContainer photoDescriptors];
-[BWDeferredContainer processingSettings];
-[BWDeferredContainer processingType];
-[BWDeferredContainer valid:];
```
