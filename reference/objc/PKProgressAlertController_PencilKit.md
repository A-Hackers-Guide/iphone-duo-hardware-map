# `PKProgressAlertController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAlertController`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"<PKProgressAlertControllerDelegate>" _delegate;
d _progress;
```

## Properties

```
@property (T@"<PKProgressAlertControllerDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_progress) progress;
```

## Class methods

```
+[PKProgressAlertController newProgressAlertControllerWithTitle:cancel:];
```

## Instance methods

```
-[PKProgressAlertController setProgress:];
-[PKProgressAlertController progress];
-[PKProgressAlertController _canShowWhileLocked];
-[PKProgressAlertController setDelegate:];
-[PKProgressAlertController delegate];
-[PKProgressAlertController canBecomeFirstResponder];
```
