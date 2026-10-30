# `PKPaletteViewHosting` (protocol)

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"UIView",R,N) hostingView;
@property (TB,R,N,GisPaletteDragging) paletteDragging;
@property (TB,N,GisPaletteVisible) paletteVisible;
@property (TB,R,N,GisPaletteVisualStateMinimized) paletteVisualStateMinimized;
@property (Td,R,N) compactPaletteAvailableWidth;
@property (T@"PKPaletteTooltipPresentationHandle",R,N) tooltipPresentationHandle;
```

## Instance methods

```
-[PKPaletteViewHosting hostingView];
-[PKPaletteViewHosting compactPaletteAvailableWidth];
-[PKPaletteViewHosting isPaletteDragging];
-[PKPaletteViewHosting isPaletteVisible];
-[PKPaletteViewHosting isPaletteVisualStateMinimized];
-[PKPaletteViewHosting setPaletteVisible:];
-[PKPaletteViewHosting tooltipPresentationHandle];
```
