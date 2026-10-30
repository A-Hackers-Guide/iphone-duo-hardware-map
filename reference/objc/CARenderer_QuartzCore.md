# `CARenderer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 19 instance methods, 2 class methods

## Instance variables

```
^v _priv;
```

## Properties

```
@property (T@"CAContext",&) context;
@property (T@"<CARendererDelegate>",W) delegate;
@property (T@"CALayer",&) layer;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}}) bounds;
```

## Class methods

```
+[CARenderer rendererWithMTLTexture:options:];
+[CARenderer rendererWithEAGLContext:options:];
```

## Instance methods

```
-[CARenderer _initWithOptions:];
-[CARenderer endFrame];
-[CARenderer layer];
-[CARenderer dealloc];
-[CARenderer setBounds:];
-[CARenderer setDestination:];
-[CARenderer setDelegate:];
-[CARenderer setContext:];
-[CARenderer delegate];
-[CARenderer bounds];
-[CARenderer context];
-[CARenderer _initWithEAGLContext:options:];
-[CARenderer _initWithMTLTexture:options:];
-[CARenderer addUpdateRect:];
-[CARenderer beginFrameAtTime:timeStamp:];
-[CARenderer nextFrameTime];
-[CARenderer render];
-[CARenderer setLayer:];
-[CARenderer updateBounds];
```
