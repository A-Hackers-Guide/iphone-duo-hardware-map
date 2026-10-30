# `BKSDisplayRenderOverlay`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BKSDisplayRenderOverlayDescribing`, `BKSDisplayRenderOverlayDismissAction`
- 1 instance variables, 12 properties, 18 instance methods, 2 class methods

## Instance variables

```
@"BKSDisplayRenderOverlayDescriptor" _descriptor;
```

## Properties

```
@property (T@"BKSDisplayRenderOverlayDescriptor",R,N,G_descriptor,V_descriptor) descriptor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) name;
@property (T@"CADisplay",R,&,N) display;
@property (Tq,R,N) interfaceOrientation;
@property (TB,R,N) lockBacklight;
@property (T@"BKSDisplayProgressIndicatorProperties",R,N) progressIndicatorProperties;
@property (TB,R,N,GisInterstitial) interstitial;
@property (T@"BKSDisplayRenderOverlayDescriptor",R,N) overlayDescriptor;
```

## Class methods

```
+[BKSDisplayRenderOverlay dismissActions];
+[BKSDisplayRenderOverlay existingOverlayForDisplay:];
```

## Instance methods

```
-[BKSDisplayRenderOverlay present];
-[BKSDisplayRenderOverlay interfaceOrientation];
-[BKSDisplayRenderOverlay display];
-[BKSDisplayRenderOverlay dismiss];
-[BKSDisplayRenderOverlay succinctDescriptionBuilder];
-[BKSDisplayRenderOverlay progressIndicatorProperties];
-[BKSDisplayRenderOverlay initWithDescriptor:];
-[BKSDisplayRenderOverlay descriptionWithMultilinePrefix:];
-[BKSDisplayRenderOverlay lockBacklight];
-[BKSDisplayRenderOverlay succinctDescription];
-[BKSDisplayRenderOverlay isInterstitial];
-[BKSDisplayRenderOverlay description];
-[BKSDisplayRenderOverlay freeze];
-[BKSDisplayRenderOverlay name];
-[BKSDisplayRenderOverlay descriptionBuilderWithMultilinePrefix:];
-[BKSDisplayRenderOverlay _descriptor];
-[BKSDisplayRenderOverlay dismissWithAnimation:];
-[BKSDisplayRenderOverlay overlayDescriptor];
```
