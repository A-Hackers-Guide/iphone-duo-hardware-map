# `UIGraphicsRenderer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 14 instance methods, 6 class methods

## Instance variables

```
@"UIGraphicsRendererFormat" _format;
@"_UIReusePool" _reusePool;
```

## Properties

```
@property (T@"UIGraphicsRendererFormat",R,N,V_format) format;
@property (TB,R,N) allowsImageOutput;
```

## Class methods

```
+[UIGraphicsRenderer rendererContextClass];
+[UIGraphicsRenderer prepareCGContext:withRendererContext:];
+[UIGraphicsRenderer contextWithFormat:];
+[UIGraphicsRenderer _destroyCGContext:withRenderer:];
+[UIGraphicsRenderer _contextWithFormat:renderer:];
+[UIGraphicsRenderer _supportsContextReuse];
```

## Instance methods

```
-[UIGraphicsRenderer pushContext:];
-[UIGraphicsRenderer initWithBounds:format:];
-[UIGraphicsRenderer runDrawingActions:completionActions:format:error:];
-[UIGraphicsRenderer runDrawingActions:completionActions:error:];
-[UIGraphicsRenderer init];
-[UIGraphicsRenderer _dequeueContextForReuse];
-[UIGraphicsRenderer popContext:];
-[UIGraphicsRenderer allowsImageOutput];
-[UIGraphicsRenderer initWithFormat:bounds:];
-[UIGraphicsRenderer _enqueueContextForReuse:];
-[UIGraphicsRenderer initWithBounds:];
-[UIGraphicsRenderer _configureReuseState];
-[UIGraphicsRenderer _prepareContextForReuse:];
-[UIGraphicsRenderer format];
```
