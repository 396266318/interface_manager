import {get_code, put_code, post_code} from "./common";


const user_path = "/backend/user/";

export const register = function(name, pwd){
  return post_code('backend/user/register', {name: name, pwd: pwd})
};

export const login = function(name, pwd){
  return post_code('backend/user/login', {name:name, pwd:pwd})
};

export const get_user = function() {
  return get_code('backend/user/get')
};
