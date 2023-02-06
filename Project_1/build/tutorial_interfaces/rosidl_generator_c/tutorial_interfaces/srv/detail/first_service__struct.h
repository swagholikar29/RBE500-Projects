// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:srv/FirstService.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__FIRST_SERVICE__STRUCT_H_
#define TUTORIAL_INTERFACES__SRV__DETAIL__FIRST_SERVICE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/FirstService in the package tutorial_interfaces.
typedef struct tutorial_interfaces__srv__FirstService_Request
{
  float x;
  float y;
  float z;
} tutorial_interfaces__srv__FirstService_Request;

// Struct for a sequence of tutorial_interfaces__srv__FirstService_Request.
typedef struct tutorial_interfaces__srv__FirstService_Request__Sequence
{
  tutorial_interfaces__srv__FirstService_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__srv__FirstService_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/FirstService in the package tutorial_interfaces.
typedef struct tutorial_interfaces__srv__FirstService_Response
{
  float q1;
  float q2;
  float q3;
} tutorial_interfaces__srv__FirstService_Response;

// Struct for a sequence of tutorial_interfaces__srv__FirstService_Response.
typedef struct tutorial_interfaces__srv__FirstService_Response__Sequence
{
  tutorial_interfaces__srv__FirstService_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__srv__FirstService_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__FIRST_SERVICE__STRUCT_H_
