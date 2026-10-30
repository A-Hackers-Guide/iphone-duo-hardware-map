# `IOSurfaceRemotePerSurfacePerClientState`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{__IOSurfaceClient=} _surface;
I _refcount;
@"IOSurfaceRemotePerSurfaceGlobalState" _globalState;
```

## Properties

```
@property (T@"IOSurfaceRemotePerSurfaceGlobalState",&,N,V_globalState) globalState;
@property (T^{__IOSurfaceClient=},R,N) surface;
@property (TI,R,N) debugRefCount;
```

## Instance methods

```
-[IOSurfaceRemotePerSurfacePerClientState surface];
-[IOSurfaceRemotePerSurfacePerClientState dealloc];
-[IOSurfaceRemotePerSurfacePerClientState mergeExtraData:];
-[IOSurfaceRemotePerSurfacePerClientState setGlobalState:];
-[IOSurfaceRemotePerSurfacePerClientState addClientReferenceToSurfaceWithExtraData:];
-[IOSurfaceRemotePerSurfacePerClientState debugRefCount];
-[IOSurfaceRemotePerSurfacePerClientState globalState];
-[IOSurfaceRemotePerSurfacePerClientState initWithSurface:mappedAddress:mappedSize:extraData:];
-[IOSurfaceRemotePerSurfacePerClientState removeClientReferenceToSurface];
```
