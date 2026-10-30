# `FMAnnotation` (protocol)

- Image: [`/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`](../userland/System__Library__PrivateFrameworks__FMCoreUI.framework__FMCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 12 properties, 24 instance methods, 0 class methods

## Properties

```
@property (T@"FMAccuracyOverlay",&,N) overlay;
@property (Td,N) horizontalAccuracy;
@property (T{CLLocationCoordinate2D=dd},N) coordinate;
@property (Td,N) distanceFromUser;
@property (TB,N) isBorderEnabled;
@property (T@"UIColor",&,N) tintColor;
@property (T@"UIImage",&,N) largeAnnotationIcon;
@property (T@"UIImage",&,N) smallAnnotationIcon;
@property (T@"UIImage",&,N) largeOverlayIcon;
@property (T@"UIImage",&,N) smallOverlayIcon;
@property (T@"NSString",?,R,C,N) title;
@property (T@"NSString",?,R,C,N) subtitle;
```

## Instance methods

```
-[FMAnnotation setOverlay:];
-[FMAnnotation coordinate];
-[FMAnnotation horizontalAccuracy];
-[FMAnnotation setHorizontalAccuracy:];
-[FMAnnotation overlay];
-[FMAnnotation setTintColor:];
-[FMAnnotation tintColor];
-[FMAnnotation isThisDevice];
-[FMAnnotation hasKnownLocation];
-[FMAnnotation isBorderEnabled];
-[FMAnnotation distanceFromUser];
-[FMAnnotation largeAnnotationIcon];
-[FMAnnotation largeOverlayIcon];
-[FMAnnotation setDistanceFromUser:];
-[FMAnnotation setIsBorderEnabled:];
-[FMAnnotation setLargeAnnotationIcon:];
-[FMAnnotation setLargeOverlayIcon:];
-[FMAnnotation setSmallAnnotationIcon:];
-[FMAnnotation setSmallOverlayIcon:];
-[FMAnnotation smallAnnotationIcon];
-[FMAnnotation smallOverlayIcon];
-[FMAnnotation subtitle];
-[FMAnnotation setCoordinate:];
-[FMAnnotation title];
```
