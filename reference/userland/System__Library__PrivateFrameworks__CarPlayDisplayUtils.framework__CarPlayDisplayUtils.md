# `/System/Library/PrivateFrameworks/CarPlayDisplayUtils.framework/CarPlayDisplayUtils`

iOS 27.2 dyld shared cache image. Version `807.4.1.0.0`. **[DSC]**

## Linked libraries (15)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/ImageIO.framework/ImageIO`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftMetal.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Swift types (22)

`CarPlayDisplayUtils.AppearanceInfo`, `CarPlayDisplayUtils.AppearanceInfo.AirPlay`, `CarPlayDisplayUtils.AppearanceInfo.DDP`, `CarPlayDisplayUtils.AppearanceMode`, `CarPlayDisplayUtils.AppearancePreference`, `CarPlayDisplayUtils.AppearanceState`, `CarPlayDisplayUtils.DisplayScaleError`, `CarPlayDisplayUtils.DisplayScaleInfo`, `CarPlayDisplayUtils.DisplayScaleInfo.Display`, `CarPlayDisplayUtils.DisplayScaleInfo.DisplaySizes`, `CarPlayDisplayUtils.DisplayScaleInfo.PointScale`, `CarPlayDisplayUtils.DisplayScaleInfo.ScaledCanvasSizes`, `CarPlayDisplayUtils.DisplayScaleInfo.ScaledCanvasSizes.CanvasSize`, `CarPlayDisplayUtils.DisplayScaleInfo.ScalingException`, `CarPlayDisplayUtils.ScreenType`, `CarPlayDisplayUtils.VehicleAppearanceSetting`, `CarPlayDisplayUtils.ViewArea`, `__C.CARDisplayScaleMode`, `__C.CGPoint`, `__C.CGRect`, `__C.CGSize`, `conformance`

## Strings (55)

```
legacy heuristic
Unsupported display scale: 
]; allowsSmartZoom: 
 suports=perDispNight
uiAppearanceMode
uiAppearanceSetting
Fatal error
Unknown display scale mode: 
com.apple.CarPlayDisplayUtils
Invalid display scale mode: .count
Unsupported display scale mode: 
Unable to parse display pixel size
Unable to parse display physical size
ScreenPhysicalSize
Connect Standard
DisplayScaleInfo: preferredPointScale: [
mapAppearanceMode
mapAppearanceSetting
CarPlayDisplayUtils/DisplayScaleInfo.swift
DisplaySizes: screenType:
No initial %{public}s: mode=%{bool,public}d setting=%{bool,public}d
nightMode: no primary screen ID, defaulting to false
nightMode: unknown screenID '%{public}s', defaulting to false
mapAppearance: unknown screenID '%{public}s'
mapAppearance: screen '%{public}s' does not support map appearance mode
canvas(%s optimal): %s × optimalFactor(%f)×scaleFactor(%f)=%f → ceilToEven = %s
optimalScaleFactor: optimalPtPerMM(%f) / ptPerMM(%f = pxW(%f)/physW(%f)) = %f
Physical size is zero, applying default size Result(%s) = PointSize(%s)/CROptimalPointsPerMM(%f)
[Appearance-Params] primary=%{bool,public}d displayNightMode=%{bool,public}d locationNightMode=%{bool,public}d uiAppearance=%{bool,public}d mapAppearance=%{bool,public}d uiAppearanceMode=%{public}s uiAppearanceSetting=%{public}s mapAppearan
Undefined => Optimal (%s)
Optimal size is within 0.05 tolerance AND not equal to the original size AND it's currently ON (new connection) AND the screen is >880x528px, we compare against smaller threshold to use 3x more often
canvas(%s optimal): %s × scaleFactor(%f)/zoom(%f)=%f → ceilToEven = %s
canvas(%s %s): %s < min %s → clamped to %s
Seeding DDP appearance for %{public}s: %{public}s
resolvedMapAppearanceMode: unknown screenID '%{public}s'
optimalScaleFactor: optimalPtPerMM(%f) / ptPerMM(%f = pxH(%f)/physH(%f)) = %f
Physical size is not valid, applying default size Result(%s) = PointSize(%s)/CROptimalPointsPerMM(%f)
Invalid initial %{public}s setting %{public}ld
resolvedAppearanceMode: unknown screenID '%{public}s'
uiAppearance: unknown screenID '%{public}s'
Will calculate DisplayScaleInfo. Using: %s, originalPointScale=%s
ScalingException: (%{public}s) match special case (%s. Scale zoomFactor set to %{public}f
Invalid initial %{public}s mode %{public}ld
Initial %{public}s: %{public}s setting:%{public}s
displayRequiresDarkAppearance: unknown screenID '%{public}s'
canvas(%s original): %s × scaleFactor(%s/%s=%f) = %s
No per-display night mode, using system: %{bool,public}d
Calculating preferred point scale for initialMode:%s. Jumping to 3x scale: pixelSize:%s, because scaledToOriginalRatio < 0.96: %f
ScalingException: (%{public}s) match special case (%s. Point Scale set to %{public}ld
Initial display night mode: %{bool,public}d
ddpAppearanceMode: unknown screenID '%{public}s', using defaults
appearancePreference: no primary screen, defaulting to automatic
uiAppearance: screen '%{public}s' does not support appearance mode
wallpaperRequiresDarkAppearance: unknown screenID '%{public}s'
Optimal,Undefined => Original (zooming in and within 5%% threshold)
```
