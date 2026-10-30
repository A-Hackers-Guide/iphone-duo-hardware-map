# `EspressoNetwork`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} _net;
```

## Properties

```
@property (T{shared_ptr<Espresso::net>=^{net}^{__shared_weak_count}},R,V_net) net;
@property (TQ,R) layers_size;
@property (T@"EspressoContext",R) ctx;
```

## Instance methods

```
-[EspressoNetwork ctx];
-[EspressoNetwork net];
-[EspressoNetwork initWithJSFile:binSerializerId:context:computePath:];
-[EspressoNetwork initWithJSFile:context:computePath:];
-[EspressoNetwork layers_size];
-[EspressoNetwork wipe_layers_blobs];
```
