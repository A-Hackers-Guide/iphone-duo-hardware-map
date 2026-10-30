# `PKToolPickerItem`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"PKTool" __tool;
```

## Properties

```
@property (T@"UIColor",&,N) color;
@property (Td,N) width;
@property (TB,R,N) _toolShouldBeSetOnCanvasView;
@property (T@"NSDictionary",R,N) _dictionaryRepresentation;
@property (T@"PKTool",&,N,V__tool) _tool;
@property (T@"NSString",R,N) identifier;
@property (T@"PKTool",R,N) tool;
```

## Instance methods

```
-[PKToolPickerItem setColor:];
-[PKToolPickerItem identifier];
-[PKToolPickerItem color];
-[PKToolPickerItem _dictionaryRepresentation];
-[PKToolPickerItem hash];
-[PKToolPickerItem setWidth:];
-[PKToolPickerItem width];
-[PKToolPickerItem copyWithZone:];
-[PKToolPickerItem tool];
-[PKToolPickerItem isEqual:];
-[PKToolPickerItem _updateTool:shouldCallObserver:];
-[PKToolPickerItem _reloadImage];
-[PKToolPickerItem _setColor:shouldCallObserver:];
-[PKToolPickerItem _setWidth:shouldCallObserver:];
-[PKToolPickerItem _tool];
-[PKToolPickerItem _toolCopyWithColor:];
-[PKToolPickerItem _toolCopyWithWidth:];
-[PKToolPickerItem _toolShouldBeSetOnCanvasView];
-[PKToolPickerItem initWithTool:];
-[PKToolPickerItem initWithTool:identifier:];
-[PKToolPickerItem set_tool:];
```
