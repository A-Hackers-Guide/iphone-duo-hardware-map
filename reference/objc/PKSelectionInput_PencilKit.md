# `PKSelectionInput`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
q _selectionType;
q _inputType;
{CGPoint="x"d"y"d} _location;
```

## Properties

```
@property (Tq,N,V_selectionType) selectionType;
@property (T{CGPoint=dd},N,V_location) location;
@property (Tq,N,V_inputType) inputType;
```

## Class methods

```
+[PKSelectionInput inputWithType:location:inputType:];
```

## Instance methods

```
-[PKSelectionInput location];
-[PKSelectionInput setSelectionType:];
-[PKSelectionInput inputType];
-[PKSelectionInput setLocation:];
-[PKSelectionInput setInputType:];
-[PKSelectionInput selectionType];
```
