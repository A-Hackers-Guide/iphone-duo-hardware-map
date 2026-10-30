# `PKDetectionView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIContextMenuInteractionDelegate_ForWebKitOnly`
- 2 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UIContextMenuInteraction" _menuInteraction;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _drawingTransform;
```

## Properties

```
@property (T@"UIContextMenuInteraction",&,N,V_menuInteraction) menuInteraction;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) drawingBounds;
@property (T{CGAffineTransform=dddddd},N,V_drawingTransform) drawingTransform;
@property (T@"PKDetectionItem",R,N) item;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKDetectionView setMenuInteraction:];
-[PKDetectionView contextMenuInteraction:configurationForMenuAtLocation:];
-[PKDetectionView init];
-[PKDetectionView accessibilityTraits];
-[PKDetectionView tapHandler:];
-[PKDetectionView drawRect:];
-[PKDetectionView menuInteraction];
-[PKDetectionView hitTest:withEvent:];
-[PKDetectionView item];
-[PKDetectionView hitTest:];
-[PKDetectionView pointInside:withEvent:];
-[PKDetectionView _contextMenuInteraction:overrideSuggestedActionsForConfiguration:];
-[PKDetectionView drawingBounds];
-[PKDetectionView _underlineColor];
-[PKDetectionView _setLineDashFor:];
-[PKDetectionView _underlineThickness];
-[PKDetectionView drawingTransform];
-[PKDetectionView setDrawingTransform:];
```
