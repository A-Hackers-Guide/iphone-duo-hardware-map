# `SBFocusEnablementIndicatorSystemApertureActivityElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FCUIFocusEnablementIndicatorSystemApertureActivityElement`
- Protocols: `SBSystemActionCoordinatedElementPreviewing`, `SBSystemActionElementPreviewing`
- 7 instance variables, 13 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBSystemActionElementPreviewingCoordinator" _previewingCoordinator;
B _displayedWithLimitedSize;
B _previewing;
B _urgent;
B _expanding;
B _prominent;
@"<SBSystemAperturePlatformElementHosting>" _platformElementHost;
```

## Properties

```
@property (TB,R,N,GisPreviewing) previewing;
@property (TB,R,N,GisUrgent) urgent;
@property (TB,R,N,GisExpanding) expanding;
@property (Tq,R,N) layoutMode;
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N,V_platformElementHost) platformElementHost;
@property (T@"<SAElementHosting>",?,W,N) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisProminent,V_prominent) prominent;
```

## Instance methods

```
-[SBFocusEnablementIndicatorSystemApertureActivityElement pop];
-[SBFocusEnablementIndicatorSystemApertureActivityElement setDisplayedWithLimitedSize:];
-[SBFocusEnablementIndicatorSystemApertureActivityElement systemApertureLayoutCustomizingOptions];
-[SBFocusEnablementIndicatorSystemApertureActivityElement setLayoutMode:reason:];
-[SBFocusEnablementIndicatorSystemApertureActivityElement isUrgent];
-[SBFocusEnablementIndicatorSystemApertureActivityElement isDisplayedWithLimitedSize];
-[SBFocusEnablementIndicatorSystemApertureActivityElement setPlatformElementHost:];
-[SBFocusEnablementIndicatorSystemApertureActivityElement isMinimalPresentationPossible];
-[SBFocusEnablementIndicatorSystemApertureActivityElement setUrgent:];
-[SBFocusEnablementIndicatorSystemApertureActivityElement setProminent:];
-[SBFocusEnablementIndicatorSystemApertureActivityElement isProminent];
-[SBFocusEnablementIndicatorSystemApertureActivityElement isPreviewing];
-[SBFocusEnablementIndicatorSystemApertureActivityElement setPreviewing:];
-[SBFocusEnablementIndicatorSystemApertureActivityElement platformElementHost];
-[SBFocusEnablementIndicatorSystemApertureActivityElement isExpanding];
-[SBFocusEnablementIndicatorSystemApertureActivityElement setExpanding:];
-[SBFocusEnablementIndicatorSystemApertureActivityElement initWithActivityDescription:enabled:];
```
