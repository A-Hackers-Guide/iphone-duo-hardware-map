# `CEKSequencedAnimation`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
d _duration;
@? _updateHandler;
@? _completionHandler;
```

## Properties

```
@property (T@"NSString",R,N,V_identifier) identifier;
@property (Td,R,N,V_duration) duration;
@property (T@?,R,C,N,V_updateHandler) updateHandler;
@property (T@?,R,C,N,V_completionHandler) completionHandler;
```

## Instance methods

```
-[CEKSequencedAnimation updateHandler];
-[CEKSequencedAnimation completionHandler];
-[CEKSequencedAnimation identifier];
-[CEKSequencedAnimation duration];
-[CEKSequencedAnimation initWithWithIdentifier:duration:updateHandler:];
-[CEKSequencedAnimation initWithWithIdentifier:duration:updateHandler:completion:];
```
