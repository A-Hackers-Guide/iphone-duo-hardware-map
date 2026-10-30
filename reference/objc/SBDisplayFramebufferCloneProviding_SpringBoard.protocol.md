# `SBDisplayFramebufferCloneProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 3 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) isFramebufferCloneAvailable;
@property (TQ,R,N) maximumSimultaneousCloneCount;
```

## Instance methods

```
-[SBDisplayFramebufferCloneProviding acquireCloneOfDisplayForWindowScene:upToAndIncludingSourceLayer:ontoWindowScene:];
-[SBDisplayFramebufferCloneProviding isFramebufferCloneAvailable];
-[SBDisplayFramebufferCloneProviding maximumSimultaneousCloneCount];
```
