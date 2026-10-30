# `UIDynamicsDebug`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `GLKViewDelegate`
- 10 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
I _vertexBuffer;
[42000{?="position"{?="x"f"y"f}"color"}] _vertices;
@"GLKBaseEffect" _effect;
@"EAGLContext" _ctx;
B _enabled;
B _showPhysics;
B _showOutlineInterior;
B _showFields;
@"UIDynamicAnimator" _animator;
@"GLKView" _debugView;
```

## Properties

```
@property (T@"UIDynamicAnimator",W,N,V_animator) animator;
@property (T@"GLKView",&,N,V_debugView) debugView;
@property (TB,N,V_enabled) enabled;
@property (TB,N,V_showPhysics) showPhysics;
@property (TB,N,V_showOutlineInterior) showOutlineInterior;
@property (TB,N,V_showFields) showFields;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDynamicsDebug setNeedsDisplay];
-[UIDynamicsDebug enabled];
-[UIDynamicsDebug init];
-[UIDynamicsDebug debugView];
-[UIDynamicsDebug setDebugView:];
-[UIDynamicsDebug dealloc];
-[UIDynamicsDebug setAnimator:];
-[UIDynamicsDebug animator];
-[UIDynamicsDebug setEnabled:];
-[UIDynamicsDebug setShowPhysics:];
-[UIDynamicsDebug _setupDebugViewIfNeccessary];
-[UIDynamicsDebug _teardownDebugView];
-[UIDynamicsDebug captureDebugInformation];
-[UIDynamicsDebug glkView:drawInRect:];
-[UIDynamicsDebug initWithAnimator:];
-[UIDynamicsDebug setShowFields:];
-[UIDynamicsDebug setShowOutlineInterior:];
-[UIDynamicsDebug showFields];
-[UIDynamicsDebug showOutlineInterior];
-[UIDynamicsDebug showPhysics];
```
