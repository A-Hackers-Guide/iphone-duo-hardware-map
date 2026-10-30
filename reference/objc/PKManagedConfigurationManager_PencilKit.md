# `PKManagedConfigurationManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 3 class methods

## Instance variables

```
@"PKManagedConfigurationState" _state;
```

## Properties

```
@property (T@"PKManagedConfigurationState",&,N,V_state) state;
```

## Class methods

```
+[PKManagedConfigurationManager sharedInstance];
+[PKManagedConfigurationManager setCurrentState:];
+[PKManagedConfigurationManager currentState];
```

## Instance methods

```
-[PKManagedConfigurationManager setState:];
-[PKManagedConfigurationManager init];
-[PKManagedConfigurationManager _managedConfigurationDidChange:];
-[PKManagedConfigurationManager state];
-[PKManagedConfigurationManager _setupState];
```
