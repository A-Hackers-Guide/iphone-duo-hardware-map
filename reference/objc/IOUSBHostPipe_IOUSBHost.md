# `IOUSBHostPipe`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOUSBHostIOSource`
- 4 instance variables, 7 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _streamsEnabled;
@"NSData" _originalDescriptorsCache;
@"NSData" _currentDescriptorsCache;
@"NSMutableSet" _invalidDescriptorCache;
```

## Properties

```
@property (T@"NSData",&,V_originalDescriptorsCache) originalDescriptorsCache;
@property (T@"NSData",&,V_currentDescriptorsCache) currentDescriptorsCache;
@property (T@"NSMutableSet",&,V_invalidDescriptorCache) invalidDescriptorCache;
@property (TB,V_streamsEnabled) streamsEnabled;
@property (Tr^{IOUSBHostIOSourceDescriptors=S{IOUSBEndpointDescriptor=CCCCSC}{IOUSBSuperSpeedEndpointCompanionDescriptor=CCCCS}{IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor=CCSI}},R) originalDescriptors;
@property (Tr^{IOUSBHostIOSourceDescriptors=S{IOUSBEndpointDescriptor=CCCCSC}{IOUSBSuperSpeedEndpointCompanionDescriptor=CCCCS}{IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor=CCSI}},R) descriptors;
@property (Td,R) idleTimeout;
```

## Instance methods

```
-[IOUSBHostPipe idleTimeout];
-[IOUSBHostPipe descriptors];
-[IOUSBHostPipe abortWithError:];
-[IOUSBHostPipe sendIORequestWithData:bytesTransferred:completionTimeout:error:];
-[IOUSBHostPipe abortWithOption:error:];
-[IOUSBHostPipe adjustPipeWithDescriptors:error:];
-[IOUSBHostPipe clearStallWithError:];
-[IOUSBHostPipe copyStreamWithStreamID:error:];
-[IOUSBHostPipe currentDescriptorsCache];
-[IOUSBHostPipe disableStreamsWithError:];
-[IOUSBHostPipe enableStreamsWithError:];
-[IOUSBHostPipe enqueueControlRequest:data:completionTimeout:error:completionHandler:];
-[IOUSBHostPipe enqueueControlRequest:data:error:completionHandler:];
-[IOUSBHostPipe enqueueControlRequest:error:completionHandler:];
-[IOUSBHostPipe enqueueIORequestWithData:completionTimeout:error:completionHandler:];
-[IOUSBHostPipe enqueueIORequestWithData:frameList:frameListCount:firstFrameNumber:error:completionHandler:];
-[IOUSBHostPipe enqueueIORequestWithData:frameList:frameListCount:firstFrameNumber:options:error:completionHandler:version:];
-[IOUSBHostPipe enqueueIORequestWithData:transactionList:transactionListCount:firstFrameNumber:options:error:completionHandler:];
-[IOUSBHostPipe initWithHostInterface:endpointAddress:deviceAddress:];
-[IOUSBHostPipe invalidDescriptorCache];
-[IOUSBHostPipe ioSourceDescriptorsWithOption:];
-[IOUSBHostPipe originalDescriptors];
-[IOUSBHostPipe originalDescriptorsCache];
-[IOUSBHostPipe sendControlRequest:data:bytesTransferred:completionTimeout:error:];
-[IOUSBHostPipe sendControlRequest:data:bytesTransferred:error:];
-[IOUSBHostPipe sendControlRequest:error:];
-[IOUSBHostPipe sendIORequestWithData:frameList:frameListCount:firstFrameNumber:error:];
-[IOUSBHostPipe sendIORequestWithData:frameList:frameListCount:firstFrameNumber:options:error:version:];
-[IOUSBHostPipe sendIORequestWithData:transactionList:transactionListCount:firstFrameNumber:options:error:];
-[IOUSBHostPipe setCurrentDescriptorsCache:];
-[IOUSBHostPipe setIdleTimeout:error:];
-[IOUSBHostPipe setInvalidDescriptorCache:];
-[IOUSBHostPipe setOriginalDescriptorsCache:];
-[IOUSBHostPipe setStreamsEnabled:];
-[IOUSBHostPipe streamsEnabled];
```
