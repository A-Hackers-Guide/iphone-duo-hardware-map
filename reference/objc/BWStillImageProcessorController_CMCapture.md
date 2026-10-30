# `BWStillImageProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWStillImageProcessorControllerInputUpdatesDelegate`
- 7 instance variables, 13 properties, 27 instance methods, 2 class methods

## Instance variables

```
@"NSString" _name;
Q _type;
@"BWStillImageProcessorControllerConfiguration" _configuration;
@"FigStateMachine" _stateMachine;
@"NSMutableArray" _requestQueue;
@"BWStillImageProcessorControllerRequest" _currentRequest;
B _hasPendingRequests;
```

## Properties

```
@property (T@"BWStillImageProcessorControllerRequest",R,N,V_currentRequest) currentRequest;
@property (TB,R,N,V_hasPendingRequests) hasPendingRequests;
@property (T@"NSString",R,N,V_name) name;
@property (TQ,R,N,V_type) type;
@property (T@"BWStillImageProcessorControllerConfiguration",R,N,V_configuration) configuration;
@property (T@"<MetalImageBufferProcessor>",R,N) metalImageBufferProcessor;
@property (TB,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryDescriptor",R,N) externalMemoryDescriptor;
@property (T@"CMIExternalMemoryResource",&,N) externalMemoryResource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWStillImageProcessorController initialize];
+[BWStillImageProcessorController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWStillImageProcessorController currentRequest];
-[BWStillImageProcessorController externalMemoryResource];
-[BWStillImageProcessorController purgeResources];
-[BWStillImageProcessorController supportsExternalMemoryResource];
-[BWStillImageProcessorController setExternalMemoryResource:];
-[BWStillImageProcessorController _reset];
-[BWStillImageProcessorController _prepare];
-[BWStillImageProcessorController process];
-[BWStillImageProcessorController dealloc];
-[BWStillImageProcessorController reset];
-[BWStillImageProcessorController initWithConfiguration:];
-[BWStillImageProcessorController configuration];
-[BWStillImageProcessorController type];
-[BWStillImageProcessorController prepare];
-[BWStillImageProcessorController metalImageBufferProcessor];
-[BWStillImageProcessorController requestForInput:delegate:errOut:];
-[BWStillImageProcessorController cancelProcessing];
-[BWStillImageProcessorController externalMemoryDescriptorForResolutionFlavors:];
-[BWStillImageProcessorController name];
-[BWStillImageProcessorController _completeCurrentRequestAndInitiateNextRequest];
-[BWStillImageProcessorController _process];
-[BWStillImageProcessorController _updateStateIfNeeded];
-[BWStillImageProcessorController currentRequestChanged];
-[BWStillImageProcessorController enqueueInputForProcessing:delegate:];
-[BWStillImageProcessorController externalMemoryDescriptor];
-[BWStillImageProcessorController hasPendingRequests];
-[BWStillImageProcessorController initWithName:type:configuration:];
```
