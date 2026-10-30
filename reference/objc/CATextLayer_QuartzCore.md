# `CATextLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 1 instance variables, 10 properties, 34 instance methods, 3 class methods

## Instance variables

```
^{CATextLayerPrivate=} _state;
```

## Properties

```
@property (T@,C) truncationString;
@property (TB,R,GisTruncated) truncated;
@property (T@,C) string;
@property (T^v) font;
@property (Td) fontSize;
@property (T^{CGColor=}) foregroundColor;
@property (TB,GisWrapped) wrapped;
@property (T@"NSString",C) truncationMode;
@property (T@"NSString",C) alignmentMode;
@property (TB) allowsFontSubpixelQuantization;
```

## Class methods

```
+[CATextLayer defaultValueForKey:];
+[CATextLayer needsDisplayForKey:];
+[CATextLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CATextLayer setForegroundColor:];
-[CATextLayer didChangeValueForKey:];
-[CATextLayer drawInContext:];
-[CATextLayer setFontSize:];
-[CATextLayer fontSize];
-[CATextLayer init];
-[CATextLayer implicitAnimationForKeyPath:];
-[CATextLayer dealloc];
-[CATextLayer setWrapped:];
-[CATextLayer truncationMode];
-[CATextLayer string];
-[CATextLayer setString:];
-[CATextLayer setAlignmentMode:];
-[CATextLayer CA_validateValue:forKey:];
-[CATextLayer font];
-[CATextLayer foregroundColor];
-[CATextLayer isWrapped];
-[CATextLayer setTruncationMode:];
-[CATextLayer alignmentMode];
-[CATextLayer setFont:];
-[CATextLayer wrapped];
-[CATextLayer _applyLinesToFunction:info:];
-[CATextLayer _applyLinesToFunction:info:truncated:];
-[CATextLayer _createStringDict];
-[CATextLayer _createTruncationToken];
-[CATextLayer _drawLine:inContext:atPoint:];
-[CATextLayer _preferredSize];
-[CATextLayer _prepareContext:];
-[CATextLayer _retainTypesetter];
-[CATextLayer allowsFontSubpixelQuantization];
-[CATextLayer isTruncated];
-[CATextLayer setAllowsFontSubpixelQuantization:];
-[CATextLayer setTruncationString:];
-[CATextLayer truncationString];
```
