# `PKDisplayLinkObserver`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"CADisplayLink" _displayLink;
@? _handler;
B _shouldStop;
```

## Instance methods

```
-[PKDisplayLinkObserver isRunning];
-[PKDisplayLinkObserver stop];
-[PKDisplayLinkObserver dealloc];
-[PKDisplayLinkObserver initWithHandler:];
-[PKDisplayLinkObserver initWithTargetTimestampHandler:];
-[PKDisplayLinkObserver _displayLinkHandler:];
-[PKDisplayLinkObserver startWithPreferredFramesPerSecond:addToRunLoop:forMode:];
```
