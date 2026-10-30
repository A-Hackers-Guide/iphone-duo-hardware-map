# `AVCaptureSessionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _configurationID;
@"NSArray" _inputs;
@"NSArray" _outputs;
@"NSPointerArray" _videoPreviewLayers;
@"NSArray" _connections;
```

## Properties

```
@property (Tq,R,V_configurationID) configurationID;
@property (T@"NSArray",R,V_inputs) inputs;
@property (T@"NSArray",R,V_outputs) outputs;
@property (T@"NSPointerArray",R,V_videoPreviewLayers) videoPreviewLayers;
@property (T@"NSArray",R,V_connections) connections;
```

## Instance methods

```
-[AVCaptureSessionConfiguration outputs];
-[AVCaptureSessionConfiguration uniqueVideoPreviewLayers:];
-[AVCaptureSessionConfiguration connections];
-[AVCaptureSessionConfiguration videoPreviewLayers];
-[AVCaptureSessionConfiguration inputs];
-[AVCaptureSessionConfiguration configurationID];
-[AVCaptureSessionConfiguration dealloc];
-[AVCaptureSessionConfiguration uniqueConnections:];
-[AVCaptureSessionConfiguration uniqueInputs:];
-[AVCaptureSessionConfiguration _videoPreviewLayersContains:];
-[AVCaptureSessionConfiguration uniqueOutputs:];
-[AVCaptureSessionConfiguration initWithConfigurationID:inputs:outputs:videoPreviewLayers:connections:];
```
