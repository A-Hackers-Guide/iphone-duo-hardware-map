# `PKDetectionItem`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_PKDrawingDetectionItem`
- 13 instance variables, 20 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _validCachedUUID;
@"NSString" _identifier;
@"PKDrawing" _drawing;
@"UIBezierPath" _itemSpaceBaselinePath;
@"UIBezierPath" _itemSpaceBoundsPath;
@"UIBezierPath" _drawingSpaceBoundsPath;
@"PKDetectionQueryItem" _queryItem;
d __strokeWidth;
@"UIColor" _inkColor;
@"PKRecognitionSessionManager" _sessionManager;
@"NSUUID" _cachedUUID;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __frame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _strokeBounds;
```

## Properties

```
@property (T@"PKDetectionQueryItem",&,N,V_queryItem) queryItem;
@property (T@"UIBezierPath",&,N,V_itemSpaceBoundsPath) itemSpaceBoundsPath;
@property (T@"UIBezierPath",&,N,V_itemSpaceBaselinePath) itemSpaceBaselinePath;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V__frame) _frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_strokeBounds) strokeBounds;
@property (Td,N,V__strokeWidth) _strokeWidth;
@property (T@"UIColor",&,N,V_inkColor) inkColor;
@property (T@"PKRecognitionSessionManager",W,N,V_sessionManager) sessionManager;
@property (T@"NSUUID",&,N,V_cachedUUID) cachedUUID;
@property (TB,N,V_validCachedUUID) validCachedUUID;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"PKDrawing",W,N,V_drawing) drawing;
@property (T@"UIColor",R,N) strokeColor;
@property (T{CGAffineTransform=dddddd},R,N) drawingToItemTransform;
@property (T@"UIBezierPath",R,N,V_drawingSpaceBoundsPath) drawingSpaceBoundsPath;
@property (T@"UIBezierPath",R,N) _baselinePath;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKDetectionItem drawing];
-[PKDetectionItem sessionManager];
-[PKDetectionItem identifier];
-[PKDetectionItem setUUID:];
-[PKDetectionItem UUID];
-[PKDetectionItem _strokeWidth];
-[PKDetectionItem _frame];
-[PKDetectionItem strokeColor];
-[PKDetectionItem setDrawing:];
-[PKDetectionItem image];
-[PKDetectionItem inkColor];
-[PKDetectionItem setInkColor:];
-[PKDetectionItem initWithSessionManager:];
-[PKDetectionItem setSessionManager:];
-[PKDetectionItem validCachedUUID];
-[PKDetectionItem _actionNameForActivation:];
-[PKDetectionItem _baselinePath];
-[PKDetectionItem _generatePaths];
-[PKDetectionItem _hitTest:];
-[PKDetectionItem _strokes];
-[PKDetectionItem cachedUUID];
-[PKDetectionItem drawingSpaceBoundsPath];
-[PKDetectionItem drawingToItemTransform];
-[PKDetectionItem handleTapForMenuForInteraction:location:view:viewTransform:drawingTransform:];
-[PKDetectionItem itemSpaceBaselinePath];
-[PKDetectionItem itemSpaceBoundsPath];
-[PKDetectionItem queryItem];
-[PKDetectionItem setCachedUUID:];
-[PKDetectionItem setItemSpaceBaselinePath:];
-[PKDetectionItem setItemSpaceBoundsPath:];
-[PKDetectionItem setQueryItem:];
-[PKDetectionItem setStrokeBounds:];
-[PKDetectionItem setValidCachedUUID:];
-[PKDetectionItem set_frame:];
-[PKDetectionItem set_strokeWidth:];
-[PKDetectionItem strokeBounds];
```
