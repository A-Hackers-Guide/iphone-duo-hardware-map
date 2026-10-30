# `CMCardioHealthManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fInternalQueue;
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} fLocationdConnection;
```

## Instance methods

```
-[CMCardioHealthManager init];
-[CMCardioHealthManager dealloc];
-[CMCardioHealthManager fetchCardioHealthDataFrom:to:dataType:handler:];
-[CMCardioHealthManager writeCardioHealthDataOfType:data:handler:];
```
