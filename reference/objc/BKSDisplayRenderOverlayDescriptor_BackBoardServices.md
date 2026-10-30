# `BKSDisplayRenderOverlayDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSSecureCoding`, `BSDescriptionProviding`, `BKSDisplayRenderOverlayDescribing`
- 7 instance variables, 11 properties, 25 instance methods, 3 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _displayUUID;
@"CADisplay" _display;
@"BKSDisplayProgressIndicatorProperties" _progressIndicatorProperties;
q _interfaceOrientation;
B _lockBacklight;
B _interstitial;
```

## Properties

```
@property (T@"NSString",C,N,V_displayUUID) displayUUID;
@property (TB,N,GisInterstitial,S_setInterstitial:,V_interstitial) interstitial;
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"CADisplay",R,N,V_display) display;
@property (Tq,N,V_interfaceOrientation) interfaceOrientation;
@property (T@"BKSDisplayProgressIndicatorProperties",&,N,V_progressIndicatorProperties) progressIndicatorProperties;
@property (TB,N,V_lockBacklight) lockBacklight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSDisplayRenderOverlayDescriptor supportsSecureCoding];
+[BKSDisplayRenderOverlayDescriptor _classesRequiredToDecode];
+[BKSDisplayRenderOverlayDescriptor descriptorWithName:display:];
```

## Instance methods

```
-[BKSDisplayRenderOverlayDescriptor interfaceOrientation];
-[BKSDisplayRenderOverlayDescriptor display];
-[BKSDisplayRenderOverlayDescriptor _setInterstitial:];
-[BKSDisplayRenderOverlayDescriptor succinctDescriptionBuilder];
-[BKSDisplayRenderOverlayDescriptor setInterfaceOrientation:];
-[BKSDisplayRenderOverlayDescriptor progressIndicatorProperties];
-[BKSDisplayRenderOverlayDescriptor _appendDescriptionToFormatterCore:];
-[BKSDisplayRenderOverlayDescriptor displayUUID];
-[BKSDisplayRenderOverlayDescriptor appendDescriptionToFormatter:];
-[BKSDisplayRenderOverlayDescriptor setProgressIndicatorProperties:];
-[BKSDisplayRenderOverlayDescriptor descriptionWithMultilinePrefix:];
-[BKSDisplayRenderOverlayDescriptor lockBacklight];
-[BKSDisplayRenderOverlayDescriptor succinctDescription];
-[BKSDisplayRenderOverlayDescriptor setDisplayUUID:];
-[BKSDisplayRenderOverlayDescriptor encodeWithCoder:];
-[BKSDisplayRenderOverlayDescriptor isInterstitial];
-[BKSDisplayRenderOverlayDescriptor hash];
-[BKSDisplayRenderOverlayDescriptor description];
-[BKSDisplayRenderOverlayDescriptor setLockBacklight:];
-[BKSDisplayRenderOverlayDescriptor initWithCoder:];
-[BKSDisplayRenderOverlayDescriptor isEqual:];
-[BKSDisplayRenderOverlayDescriptor _initWithName:displayUUID:];
-[BKSDisplayRenderOverlayDescriptor name];
-[BKSDisplayRenderOverlayDescriptor initWithName:display:];
-[BKSDisplayRenderOverlayDescriptor descriptionBuilderWithMultilinePrefix:];
```
