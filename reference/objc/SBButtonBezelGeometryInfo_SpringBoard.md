# `SBButtonBezelGeometryInfo`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 8 instance methods, 2 class methods

## Instance variables

```
q _surfaceType;
B _coverInUseWhileUnfolded;
```

## Class methods

```
+[SBButtonBezelGeometryInfo buttonBezelGeometryInfoForCurrentEmbeddedDisplayBezel];
+[SBButtonBezelGeometryInfo buttonBezelGeometryInfoForWindowScene:];
```

## Instance methods

```
-[SBButtonBezelGeometryInfo _displayIndex];
-[SBButtonBezelGeometryInfo _initWithSurfaceType:coverInUseWhileUnfolded:];
-[SBButtonBezelGeometryInfo _naturalNormalizedButtonHWRectForButton:];
-[SBButtonBezelGeometryInfo buttonHWRectForButton:inView:];
-[SBButtonBezelGeometryInfo buttonHWRectForButton:onEmbeddedDisplayBounds:];
-[SBButtonBezelGeometryInfo buttonScreenEdgeForButton:];
-[SBButtonBezelGeometryInfo isPhysicalButtonOnDisplayEdge:];
-[SBButtonBezelGeometryInfo normalizedButtonHWRectForButton:];
```
