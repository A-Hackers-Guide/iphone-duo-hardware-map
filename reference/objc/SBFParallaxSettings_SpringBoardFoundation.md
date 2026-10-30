# `SBFParallaxSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISettings`
- 14 instance variables, 14 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _slideEnabled;
B _tiltEnabled;
B _increaseEnabled;
q _slideDirectionX;
q _slideDirectionY;
d _slidePixelsX;
d _slidePixelsY;
q _tiltDirectionX;
q _tiltDirectionY;
d _tiltDegreesX;
d _tiltDegreesY;
q _distanceFromScreen;
d _slideIncreaseX;
d _slideIncreaseY;
```

## Properties

```
@property (TB,V_slideEnabled) slideEnabled;
@property (Tq,V_slideDirectionX) slideDirectionX;
@property (Tq,V_slideDirectionY) slideDirectionY;
@property (Td,V_slidePixelsX) slidePixelsX;
@property (Td,V_slidePixelsY) slidePixelsY;
@property (TB,V_tiltEnabled) tiltEnabled;
@property (Tq,V_tiltDirectionX) tiltDirectionX;
@property (Tq,V_tiltDirectionY) tiltDirectionY;
@property (Td,V_tiltDegreesX) tiltDegreesX;
@property (Td,V_tiltDegreesY) tiltDegreesY;
@property (Tq,V_distanceFromScreen) distanceFromScreen;
@property (TB,V_increaseEnabled) increaseEnabled;
@property (Td,V_slideIncreaseX) slideIncreaseX;
@property (Td,V_slideIncreaseY) slideIncreaseY;
```

## Class methods

```
+[SBFParallaxSettings settingsControllerModule];
```

## Instance methods

```
-[SBFParallaxSettings setTiltEnabled:];
-[SBFParallaxSettings setDefaultValues];
-[SBFParallaxSettings slideDirectionX];
-[SBFParallaxSettings increaseEnabled];
-[SBFParallaxSettings slideDirectionY];
-[SBFParallaxSettings distanceFromScreen];
-[SBFParallaxSettings setDistanceFromScreen:];
-[SBFParallaxSettings setIncreaseEnabled:];
-[SBFParallaxSettings setSlideDirectionX:];
-[SBFParallaxSettings setSlideDirectionY:];
-[SBFParallaxSettings setSlideEnabled:];
-[SBFParallaxSettings setSlideIncreaseX:];
-[SBFParallaxSettings setSlideIncreaseY:];
-[SBFParallaxSettings setSlidePixelsX:];
-[SBFParallaxSettings setSlidePixelsY:];
-[SBFParallaxSettings setTiltDegreesX:];
-[SBFParallaxSettings setTiltDegreesY:];
-[SBFParallaxSettings setTiltDirectionX:];
-[SBFParallaxSettings setTiltDirectionY:];
-[SBFParallaxSettings slideEnabled];
-[SBFParallaxSettings slideIncreaseX];
-[SBFParallaxSettings slideIncreaseY];
-[SBFParallaxSettings slidePixelsX];
-[SBFParallaxSettings slidePixelsY];
-[SBFParallaxSettings tiltDegreesX];
-[SBFParallaxSettings tiltDegreesY];
-[SBFParallaxSettings tiltDirectionX];
-[SBFParallaxSettings tiltDirectionY];
-[SBFParallaxSettings tiltEnabled];
```
