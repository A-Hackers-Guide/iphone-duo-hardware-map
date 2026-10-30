# `BiometricKitEnrollProgressInfo`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
i _message;
q _progress;
q _currentPrimaryComponentID;
@"NSDictionary" _captureImage;
@"NSDictionary" _renderedImage;
@"NSDictionary" _messageDetails;
```

## Properties

```
@property (Tq,N,V_progress) progress;
@property (Tq,N,V_currentPrimaryComponentID) currentPrimaryComponentID;
@property (T@"NSDictionary",&,N,V_captureImage) captureImage;
@property (T@"NSDictionary",&,N,V_renderedImage) renderedImage;
@property (Ti,N,V_message) message;
@property (T@"NSDictionary",&,N,V_messageDetails) messageDetails;
```

## Instance methods

```
-[BiometricKitEnrollProgressInfo setMessage:];
-[BiometricKitEnrollProgressInfo setProgress:];
-[BiometricKitEnrollProgressInfo init];
-[BiometricKitEnrollProgressInfo message];
-[BiometricKitEnrollProgressInfo dealloc];
-[BiometricKitEnrollProgressInfo renderedImage];
-[BiometricKitEnrollProgressInfo progress];
-[BiometricKitEnrollProgressInfo captureImage];
-[BiometricKitEnrollProgressInfo currentPrimaryComponentID];
-[BiometricKitEnrollProgressInfo messageDetails];
-[BiometricKitEnrollProgressInfo setCaptureImage:];
-[BiometricKitEnrollProgressInfo setCurrentPrimaryComponentID:];
-[BiometricKitEnrollProgressInfo setMessageDetails:];
-[BiometricKitEnrollProgressInfo setRenderedImage:];
```
