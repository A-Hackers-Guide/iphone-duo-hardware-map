# `TUCaptionsClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCCaptionsClientDelegate`, `TUCallCenterDelegate`
- 2 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<TUCaptionsClientDelegate>" _delegate;
@"AVCCaptionsClient" _avcCaptionsClient;
```

## Properties

```
@property (T@"<TUCaptionsClientDelegate>",R,V_delegate) delegate;
@property (T@"AVCCaptionsClient",R,V_avcCaptionsClient) avcCaptionsClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUCaptionsClient enableCaptions:];
-[TUCaptionsClient delegate];
-[TUCaptionsClient avcCaptionsClient];
-[TUCaptionsClient callCenter:receivedCaptions:];
-[TUCaptionsClient captionsClient:didDetectGibberish:];
-[TUCaptionsClient captionsClient:didDisableCaptions:error:];
-[TUCaptionsClient captionsClient:didEnableCaptions:error:];
-[TUCaptionsClient captionsClient:didStartCaptioningWithReason:];
-[TUCaptionsClient captionsClient:didStopCaptioningWithReason:];
-[TUCaptionsClient captionsClient:didUpdateCaptions:source:];
-[TUCaptionsClient captionsServerDidDie:];
-[TUCaptionsClient configureCaptions:];
-[TUCaptionsClient initWithDelegate:call:];
```
