// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:srv/FirstService.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__FIRST_SERVICE__BUILDER_HPP_
#define TUTORIAL_INTERFACES__SRV__DETAIL__FIRST_SERVICE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/srv/detail/first_service__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace srv
{

namespace builder
{

class Init_FirstService_Request_z
{
public:
  explicit Init_FirstService_Request_z(::tutorial_interfaces::srv::FirstService_Request & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::srv::FirstService_Request z(::tutorial_interfaces::srv::FirstService_Request::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::srv::FirstService_Request msg_;
};

class Init_FirstService_Request_y
{
public:
  explicit Init_FirstService_Request_y(::tutorial_interfaces::srv::FirstService_Request & msg)
  : msg_(msg)
  {}
  Init_FirstService_Request_z y(::tutorial_interfaces::srv::FirstService_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_FirstService_Request_z(msg_);
  }

private:
  ::tutorial_interfaces::srv::FirstService_Request msg_;
};

class Init_FirstService_Request_x
{
public:
  Init_FirstService_Request_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FirstService_Request_y x(::tutorial_interfaces::srv::FirstService_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_FirstService_Request_y(msg_);
  }

private:
  ::tutorial_interfaces::srv::FirstService_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::FirstService_Request>()
{
  return tutorial_interfaces::srv::builder::Init_FirstService_Request_x();
}

}  // namespace tutorial_interfaces


namespace tutorial_interfaces
{

namespace srv
{

namespace builder
{

class Init_FirstService_Response_q3
{
public:
  explicit Init_FirstService_Response_q3(::tutorial_interfaces::srv::FirstService_Response & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::srv::FirstService_Response q3(::tutorial_interfaces::srv::FirstService_Response::_q3_type arg)
  {
    msg_.q3 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::srv::FirstService_Response msg_;
};

class Init_FirstService_Response_q2
{
public:
  explicit Init_FirstService_Response_q2(::tutorial_interfaces::srv::FirstService_Response & msg)
  : msg_(msg)
  {}
  Init_FirstService_Response_q3 q2(::tutorial_interfaces::srv::FirstService_Response::_q2_type arg)
  {
    msg_.q2 = std::move(arg);
    return Init_FirstService_Response_q3(msg_);
  }

private:
  ::tutorial_interfaces::srv::FirstService_Response msg_;
};

class Init_FirstService_Response_q1
{
public:
  Init_FirstService_Response_q1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FirstService_Response_q2 q1(::tutorial_interfaces::srv::FirstService_Response::_q1_type arg)
  {
    msg_.q1 = std::move(arg);
    return Init_FirstService_Response_q2(msg_);
  }

private:
  ::tutorial_interfaces::srv::FirstService_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::FirstService_Response>()
{
  return tutorial_interfaces::srv::builder::Init_FirstService_Response_q1();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__FIRST_SERVICE__BUILDER_HPP_
