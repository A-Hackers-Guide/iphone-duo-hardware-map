# `CAMFocusResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _performingContrastDetection;
B _contrastBasedFocusDidStart;
B _contrastBasedFocusDidEnd;
B _deviceSupportsFocus;
q _focusMode;
{CGPoint="x"d"y"d} _pointOfInterest;
```

## Properties

```
@property (TB,R,N,GisPerformingContrastDetection,V_performingContrastDetection) performingContrastDetection;
@property (T{CGPoint=dd},R,N,V_pointOfInterest) pointOfInterest;
@property (Tq,R,N,V_focusMode) focusMode;
@property (TB,R,N,V_contrastBasedFocusDidStart) contrastBasedFocusDidStart;
@property (TB,R,N,V_contrastBasedFocusDidEnd) contrastBasedFocusDidEnd;
@property (TB,R,N,V_deviceSupportsFocus) deviceSupportsFocus;
```

## Instance methods

```
-[CAMFocusResult description];
-[CAMFocusResult focusMode];
-[CAMFocusResult pointOfInterest];
-[CAMFocusResult contrastBasedFocusDidEnd];
-[CAMFocusResult contrastBasedFocusDidStart];
-[CAMFocusResult deviceSupportsFocus];
-[CAMFocusResult initWithMode:pointOfInterest:performingContrastDetection:contrastBasedFocusDidStart:contrastBasedFocusDidEnd:deviceSupportsFocus:];
-[CAMFocusResult isPerformingContrastDetection];
```
