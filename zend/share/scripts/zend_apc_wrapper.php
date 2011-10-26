<?php

/**
 * APC API Wrapper for Zend Data Cache
 *
 * This script will define APC-like wrapper functions for use with the Zend 
 * Data Cache API. This will allow APC users to replace APC with Zend Data 
 * Cache without changing their code.
 * 
 * In order to use, simply include this file at the top of any request that
 * uses any APC API function. It is also possible to set auto_prepend_file in
 * php.ini to point to this file - this will make sure the file is 
 * automatically included in all PHP requests.
 *  
 * Including this script should have no side effects if APC is loaded, and will
 * define the wrapper functions only if APC is not loaded and Zend Data Cache 
 * is.
 * 
 * @copyright 
 * @license   
 * @link      
 */

if (! function_exists("apc_store") && function_exists('zend_shm_cache_store')) {
    
    /**
     * Store an item in cache
     *
     * @param  string  $key
     * @param  mixed   $var
     * @param  integer $ttl
     * @return boolean
     */
    function apc_store($key, $var, $ttl)
    {
        return zend_shm_cache_store($key, $var, $ttl);
    }
    
    /**
     * Set a new value to an existing item in cache
     *
     * @param  string  $key
     * @param  mixed   $var
     * @param  integer $ttl
     * @return boolean
     */
    function apc_add($key, $var, $ttl)
    {
        if (zend_shm_cache_fetch($key) === NULL) {
            return zend_shm_cache_store($key, $var, $ttl);
        } else {
            return false;
        }
    }
    
    /**
     * Fetch a value from the cache
     *
     * @param  string $key
     * @return mixed
     */
    function apc_fetch($key)
    {
        return zend_shm_cache_fetch($key);
    }
    
    /**
     * Delete an item from the cache
     *
     * @param  string $key
     * @return boolean
     */
    function apc_delete($key)
    {
        return zend_shm_cache_delete($key);
    }
    
    /**
     * Clear the entire cache
     *
     * @return boolean
     */
    function apc_clear_cache()
    {
        return zend_shm_cache_clear();
    }
}
