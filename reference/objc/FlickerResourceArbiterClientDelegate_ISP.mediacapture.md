# `FlickerResourceArbiterClientDelegate`

- Image: [`/System/Library/MediaCapture/ISP.mediacapture`](../userland/System__Library__MediaCapture__ISP.mediacapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ResourceArbiterClientDelegate`
- 3 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _contextMutex;
@"ResourceArbiterClient" _arbiterClient;
^{ISPFlickerDetectorContext=^{ISPFlickerDetectorHWInfoStruct}B^{OpaqueAudioComponentInstance}{AudioStreamBasicDescription=dIIIIIIII}I{AudioBuffer=II^v}{AudioBuffer=II^v}Q{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}^{CPastFlickerHistory}i^{OpaqueFFTSetup}{ISPFlickerDetectorDebugContext=^{__sFILE}^{__sFILE}^{__sFILE}^{__sFILE}^{__sFILE}^{ISPMetrics}^{photometer_flicker_result}}f^?^vB{_opaque_pthread_mutex_t=q[56c]}@f^{?}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}CI^{AppleCameraPhotonDetectorServicesAssistant}[132C][24C]} _flickerContext;
```

## Properties

```
@property (T@"ResourceArbiterClient",R,N,V_arbiterClient) arbiterClient;
@property (T^{ISPFlickerDetectorContext=^{ISPFlickerDetectorHWInfoStruct}B^{OpaqueAudioComponentInstance}{AudioStreamBasicDescription=dIIIIIIII}I{AudioBuffer=II^v}{AudioBuffer=II^v}Q{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}^{CPastFlickerHistory}i^{OpaqueFFTSetup}{ISPFlickerDetectorDebugContext=^{__sFILE}^{__sFILE}^{__sFILE}^{__sFILE}^{__sFILE}^{ISPMetrics}^{photometer_flicker_result}}f^?^vB{_opaque_pthread_mutex_t=q[56c]}@f^{?}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}CI^{AppleCameraPhotonDetectorServicesAssistant}[132C][24C]},N,V_flickerContext) flickerContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FlickerResourceArbiterClientDelegate cleanup];
-[FlickerResourceArbiterClientDelegate init];
-[FlickerResourceArbiterClientDelegate dealloc];
-[FlickerResourceArbiterClientDelegate arbiterClient];
-[FlickerResourceArbiterClientDelegate flickerContext];
-[FlickerResourceArbiterClientDelegate releaseResourceAccess];
-[FlickerResourceArbiterClientDelegate requestResourceAccess];
-[FlickerResourceArbiterClientDelegate resourceAccessResult:];
-[FlickerResourceArbiterClientDelegate resourceAccessRevoked];
-[FlickerResourceArbiterClientDelegate setFlickerContext:];
```
