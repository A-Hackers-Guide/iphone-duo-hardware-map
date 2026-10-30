# `IOKObject`

- Image: [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](../userland/System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
I _object;
```

## Properties

```
@property (T@"NSString",R,C,N) ioClassName;
@property (TI,R,N,V_object) object;
```

## Class methods

```
+[IOKObject bundleIdentifierForClassName:];
+[IOKObject classForRegistryEntry:];
+[IOKObject ioSuperClassNameForClassName:];
```

## Instance methods

```
-[IOKObject init];
-[IOKObject dealloc];
-[IOKObject hash];
-[IOKObject isEqual:];
-[IOKObject object];
-[IOKObject conformsToIOClassName:];
-[IOKObject ioClassName];
-[IOKObject initWithIOObject:];
```
