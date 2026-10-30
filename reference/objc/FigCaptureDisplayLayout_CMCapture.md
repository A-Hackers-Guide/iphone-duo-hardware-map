# `FigCaptureDisplayLayout`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 32 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
q _displayType;
q _interfaceOrientation;
q _displayRegion;
@"NSArray" _foregroundApps;
@"NSArray" _obscuredApps;
@"NSArray" _transitioningApps;
@"NSArray" _pipApps;
B _onHomeScreen;
B _onLockScreen;
B _siriVisible;
B _campoVisible;
B _paymentServiceVisible;
B _paymentServiceIDVerifierVisible;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (Tq,N,V_displayType) displayType;
@property (Tq,N,V_interfaceOrientation) interfaceOrientation;
@property (Tq,N,V_displayRegion) displayRegion;
@property (T@"NSArray",&,N,V_foregroundApps) foregroundApps;
@property (T@"NSArray",&,N,V_obscuredApps) obscuredApps;
@property (T@"NSArray",&,N,V_transitioningApps) transitioningApps;
@property (T@"NSArray",&,N,V_pipApps) pipApps;
@property (TB,N,GisOnHomeScreen,V_onHomeScreen) onHomeScreen;
@property (TB,N,GisOnLockScreen,V_onLockScreen) onLockScreen;
@property (TB,N,GisSiriVisible,V_siriVisible) siriVisible;
@property (TB,N,GisCampoVisible,V_campoVisible) campoVisible;
@property (TB,N,GisPaymentServiceVisible,V_paymentServiceVisible) paymentServiceVisible;
@property (TB,N,GisPaymentServiceIDVerifierVisible,V_paymentServiceIDVerifierVisible) paymentServiceIDVerifierVisible;
```

## Class methods

```
+[FigCaptureDisplayLayout initialize];
```

## Instance methods

```
-[FigCaptureDisplayLayout isOnLockScreen];
-[FigCaptureDisplayLayout setTransitioningApps:];
-[FigCaptureDisplayLayout interfaceOrientation];
-[FigCaptureDisplayLayout setTimestamp:];
-[FigCaptureDisplayLayout setDisplayRegion:];
-[FigCaptureDisplayLayout displayRegion];
-[FigCaptureDisplayLayout setDisplayType:];
-[FigCaptureDisplayLayout displayType];
-[FigCaptureDisplayLayout debugDescription];
-[FigCaptureDisplayLayout setObscuredApps:];
-[FigCaptureDisplayLayout setInterfaceOrientation:];
-[FigCaptureDisplayLayout setPaymentServiceIDVerifierVisible:];
-[FigCaptureDisplayLayout setPaymentServiceVisible:];
-[FigCaptureDisplayLayout dealloc];
-[FigCaptureDisplayLayout timestamp];
-[FigCaptureDisplayLayout setCampoVisible:];
-[FigCaptureDisplayLayout setSiriVisible:];
-[FigCaptureDisplayLayout _init];
-[FigCaptureDisplayLayout isPaymentServiceVisible];
-[FigCaptureDisplayLayout isOnHomeScreen];
-[FigCaptureDisplayLayout isCampoVisible];
-[FigCaptureDisplayLayout obscuredApps];
-[FigCaptureDisplayLayout isSiriVisible];
-[FigCaptureDisplayLayout setPipApps:];
-[FigCaptureDisplayLayout description];
-[FigCaptureDisplayLayout isPaymentServiceIDVerifierVisible];
-[FigCaptureDisplayLayout setForegroundApps:];
-[FigCaptureDisplayLayout transitioningApps];
-[FigCaptureDisplayLayout pipApps];
-[FigCaptureDisplayLayout foregroundApps];
-[FigCaptureDisplayLayout setOnLockScreen:];
-[FigCaptureDisplayLayout setOnHomeScreen:];
```
