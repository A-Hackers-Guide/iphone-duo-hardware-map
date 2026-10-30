# `BWStillImageBufferRouterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 13 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _usingBravoDevice;
B _usingPearlDevice;
B _HDRSupported;
B _SISSupported;
B _GNRSISSupported;
B _LTMHDRSupported;
@"NSArray" _inputPortTypes;
@"NSDictionary" _portTypeToInput;
@"BWNodeOutput" _defaultOutput;
@"BWNodeOutput" _HDROutput;
@"BWNodeOutput" _SISOutput;
@"BWNodeOutput" _bravoTelephotoOutput;
@"BWNodeOutput" _pearlInfraredOutput;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_defaultOutput) defaultOutput;
@property (T@"BWNodeOutput",R,N,V_HDROutput) HDROutput;
@property (T@"BWNodeOutput",R,N,V_SISOutput) SISOutput;
@property (T@"BWNodeOutput",R,N,V_bravoTelephotoOutput) bravoTelephotoOutput;
@property (T@"BWNodeOutput",R,N,V_pearlInfraredOutput) pearlInfraredOutput;
```

## Class methods

```
+[BWStillImageBufferRouterNode initialize];
```

## Instance methods

```
-[BWStillImageBufferRouterNode renderSampleBuffer:forInput:];
-[BWStillImageBufferRouterNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWStillImageBufferRouterNode inputForPortType:];
-[BWStillImageBufferRouterNode dealloc];
-[BWStillImageBufferRouterNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWStillImageBufferRouterNode nodeSubType];
-[BWStillImageBufferRouterNode didSelectFormat:forInput:];
-[BWStillImageBufferRouterNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageBufferRouterNode handleNodeError:forInput:];
-[BWStillImageBufferRouterNode nodeType];
-[BWStillImageBufferRouterNode HDROutput];
-[BWStillImageBufferRouterNode SISOutput];
-[BWStillImageBufferRouterNode bravoTelephotoOutput];
-[BWStillImageBufferRouterNode defaultOutput];
-[BWStillImageBufferRouterNode didReachEndOfDataForInput:];
-[BWStillImageBufferRouterNode initWithInputPortTypes:HDRSupported:SISSupported:GNRSISSupported:LTMHDRSupported:depthDataDeliveryEnabled:];
-[BWStillImageBufferRouterNode pearlInfraredOutput];
```
