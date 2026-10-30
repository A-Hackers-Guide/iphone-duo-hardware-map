# `CAMetalDisplayLinkUpdate`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"<CAMetalDrawable>" _drawable;
d _targetTimestamp;
d _targetPresentationTimestamp;
```

## Properties

```
@property (T@"<CAMetalDrawable>",R,N,V_drawable) drawable;
@property (Td,R,N,V_targetTimestamp) targetTimestamp;
@property (Td,R,N,V_targetPresentationTimestamp) targetPresentationTimestamp;
```

## Class methods

```
+[CAMetalDisplayLinkUpdate updateWithDrawable:targetTimestamp:targetPresentationTimestamp:];
```

## Instance methods

```
-[CAMetalDisplayLinkUpdate targetTimestamp];
-[CAMetalDisplayLinkUpdate targetPresentationTimestamp];
-[CAMetalDisplayLinkUpdate dealloc];
-[CAMetalDisplayLinkUpdate drawable];
```
