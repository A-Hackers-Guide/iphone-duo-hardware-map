# `IOUSBHostStream`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOUSBHostIOSource`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"IOUSBHostPipe" _hostPipe;
Q _streamID;
```

## Properties

```
@property (T@"IOUSBHostPipe",&,V_hostPipe) hostPipe;
@property (TQ,V_streamID) streamID;
```

## Instance methods

```
-[IOUSBHostStream streamID];
-[IOUSBHostStream setStreamID:];
-[IOUSBHostStream abortWithError:];
-[IOUSBHostStream abortWithOption:error:];
-[IOUSBHostStream enqueueIORequestWithData:error:completionHandler:];
-[IOUSBHostStream hostPipe];
-[IOUSBHostStream initWithHostPipe:streamID:];
-[IOUSBHostStream sendIORequestWithData:bytesTransferred:error:];
-[IOUSBHostStream setHostPipe:];
```
