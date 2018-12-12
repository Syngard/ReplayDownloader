import os, request


# TODO : Class Downloader


class Downloader():
    """Generic dowload class for all replay website"""
        

    def default_filename():
        """ TODO : Generate filename based on the video title.
            For now just a fixed string
        :rtype: str
        :returns:
            An os file system compatible filename.
        """
        return 'default.mp4'

    def download(self, url, output_path=None, filename=None, filename_prefix=None):
        """Write the media stream to disk.
        :param output_path:
            (optional) Output path for writing media file. If one is not
            specified, defaults to the current working directory.
        :type output_path: str or None
        :param filename:
            (optional) Output filename (stem only) for writing media file.
            If one is not specified, the default filename is used.
        :type filename: str or None
        :param filename_prefix:
            (optional) A string that will be prepended to the filename.
            For example a number in a playlist or the name of a series.
            If one is not specified, nothing will be prepended
            This is seperate from filename so you can use the default
            filename but still add a prefix.
        :type filename_prefix: str or None
        :rtype: str
        """
        output_path = output_path or os.getcwd()
        
        """
        if filename:
            safe = safe_filename(filename)
            filename = '{filename}.{s.subtype}'.format(filename=safe, s=self)
        """
        filename = filename or default_filename()

        if filename_prefix:
            filename = '{prefix}{filename}'\
                .format(
                    prefix=safe_filename(filename_prefix),
                    filename=filename,
                )

        # file path
        fp = os.path.join(output_path, filename)
        bytes_remaining = request.file_size(url) #self.filesize
        
        with open(fp, 'wb') as fh:
            for chunk in request.get(url, streaming=True):
                # reduce the (bytes) remainder by the length of the chunk.
                bytes_remaining -= len(chunk)
                # send to the on_progress callback.
                self.on_progress(chunk, fh, bytes_remaining)
        #on_complete(fh)
        return fp


    def on_progress(self,chunk, file_handler, bytes_remaining):
        """On progress callback function.
        This function writes the binary data to the file, then checks if an
        additional callback is defined in the monostate. This is exposed to
        allow things like displaying a progress bar.
        :param str chunk:
            Segment of media file binary data, not yet written to disk.
        :param file_handler:
            The file handle where the media is being written to.
        :type file_handler:
            :py:class:`io.BufferedWriter`
        :param int bytes_remaining:
            The delta between the total file size in bytes and amount already
            downloaded.
        :rtype: None
        """
        file_handler.write(chunk)
        
        """
        on_progress = self._monostate['on_progress']
        if on_progress:
            logger.debug('calling on_progress callback %s', on_progress)
            on_progress(self, chunk, file_handler, bytes_remaining)
        """

